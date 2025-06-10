from terrymath import TerryMath, TerryVector2, TerryVector3
from terrylinalg import TerryQuaternion

class TerryBody:
    def __init__(self, position, velocity, mass, math_engine=None, is_static=False):
        self.math = math_engine or TerryMath()
        self.position = position  # TerryVector2 or TerryVector3
        self.velocity = velocity  # TerryVector2 or TerryVector3
        self.mass = mass
        self.force_accum = self.zero_vector()
        self.is_static = is_static

    def zero_vector(self):
        if isinstance(self.position, TerryVector3):
            return TerryVector3(0, 0, 0, self.math)
        else:
            return TerryVector2(0, 0, self.math)

    def apply_force(self, force):
        self.force_accum = self.force_accum + force

    def apply_impulse(self, impulse):
        if not self.is_static:
            self.velocity = self.velocity + (impulse * self.math.terry_divide(1, self.mass))

    def integrate(self, dt, friction=0.0):
        if self.is_static:
            return
        # Newton's Second Law: F = m * a => a = F / m
        acceleration = self.force_accum * self.math.terry_divide(1, self.mass)
        self.velocity = self.velocity + (acceleration * dt)
        # Apply friction (simple model)
        if friction > 0.0:
            self.velocity = self.velocity * (1 - friction)
        self.position = self.position + (self.velocity * dt)
        self.force_accum = self.zero_vector()

    def momentum(self):
        """Linear momentum: p = m * v"""
        return self.velocity * self.mass

    def kinetic_energy(self):
        """Translational kinetic energy: KE = 0.5 * m * v^2"""
        v2 = self.velocity.dot(self.velocity)
        return self.math.terry_multiply(
            self.math.terry_multiply(0.5, self.mass),
            v2
        )

    def potential_energy(self, gravity_vector):
        # PE = m * g * h (h = projection of position onto gravity direction)
        g_mag = (gravity_vector.dot(gravity_vector)) ** 0.5
        if g_mag == 0:
            return 0
        h = self.position.dot(gravity_vector) / g_mag
        return self.math.terry_multiply(self.mass, self.math.terry_multiply(g_mag, h))

    def __repr__(self):
        return f"TerryBody(pos={self.position}, vel={self.velocity}, mass={self.mass})"

class TerryWorld:
    def __init__(self, math_engine=None, gravity=None, friction=0.0):
        self.math = math_engine or TerryMath()
        self.bodies = []
        self.gravity = gravity  # TerryVector2 or TerryVector3 or None
        self.friction = friction

    def add_body(self, body):
        self.bodies.append(body)

    def apply_gravity(self):
        if self.gravity is not None:
            for body in self.bodies:
                if not body.is_static:
                    body.apply_force(self.gravity * body.mass)

    def apply_newtonian_gravity(self, G=1.0):
        # Universal gravitation: F = G * m1 * m2 / r^2
        n = len(self.bodies)
        for i in range(n):
            for j in range(i+1, n):
                a = self.bodies[i]
                b = self.bodies[j]
                if a.is_static and b.is_static:
                    continue
                r_vec = b.position - a.position
                r2 = r_vec.dot(r_vec)
                if r2 == 0:
                    continue  # Avoid division by zero
                force_mag = self.math.terry_divide(
                    self.math.terry_multiply(G, self.math.terry_multiply(a.mass, b.mass)),
                    r2
                )
                # Direction: normalized r_vec
                r_len = r2 ** 0.5
                direction = r_vec * (1.0 / r_len)
                force = direction * force_mag
                a.apply_force(force)
                b.apply_force(force * -1)  # Newton's Third Law

    def step(self, dt):
        # Newton's First Law: If no force, velocity stays the same
        self.apply_gravity()
        self.apply_newtonian_gravity(G=1.0)
        for body in self.bodies:
            body.integrate(dt, friction=self.friction)

    def elastic_collision(self, body_a, body_b, normal):
        # 1D/2D/3D elastic collision along normal vector
        tm = self.math
        rel_vel = body_b.velocity - body_a.velocity
        vel_along_normal = rel_vel.dot(normal)
        if vel_along_normal > 0:
            return  # Bodies are separating
        m1, m2 = body_a.mass, body_b.mass
        e = 1.0  # Coefficient of restitution (perfectly elastic)
        j = tm.terry_divide(
            tm.terry_multiply(-(1 + e), vel_along_normal),
            tm.terry_add(m1, m2)
        )
        impulse = normal * j
        body_a.apply_impulse(-impulse)
        body_b.apply_impulse(impulse)

class TerryRigidBody(TerryBody):
    """
    TerryRigidBody extends TerryBody with angular motion.
    Linear: position, velocity (from TerryBody)
    Angular: orientation (quaternion), angular_velocity, torque, inertia
    """
    def __init__(
        self,
        position,
        velocity,
        mass,
        orientation=None,
        angular_velocity=None,
        inertia=1.0,
        collision_shape=None,
        math_engine=None,
        is_static=False
    ):
        super().__init__(position, velocity, mass, math_engine, is_static)
        tm = self.math
        self.orientation = orientation or TerryQuaternion(1, 0, 0, 0, tm)
        self.angular_velocity = angular_velocity or TerryVector3(0, 0, 0, tm)
        self.torque_accum = TerryVector3(0, 0, 0, tm)
        self._inertia = inertia
        self.collision_shape = collision_shape
        self.sleeping = False  # <-- Add this line

    def set_sleeping(self, sleeping=True):
        """Set the sleeping state of the rigid body."""
        self.sleeping = sleeping

    def wake(self):
        """Wake up the rigid body (set sleeping to False)."""
        self.sleeping = False

    def is_sleeping(self):
        """Return True if the body is sleeping."""
        return self.sleeping

    @property
    def inertia(self):
        """Moment of inertia (scalar for now, can be replaced with tensor/matrix)."""
        return self._inertia

    @inertia.setter
    def inertia(self, value):
        self._inertia = value

    def apply_force(self, force, point=None):
        """
        Apply a force to the rigid body.
        If 'point' is given (as a TerryVector3), applies torque as well (force at offset).
        """
        super().apply_force(force)
        if point is not None:
            # r = point - position
            r = point - self.position
            torque = r.cross(force)
            self.apply_torque(torque)

    def apply_torque(self, torque):
        """
        Apply a torque (TerryVector3) to the rigid body.
        """
        self.torque_accum = self.torque_accum + torque

    def integrate(self, dt, friction=0.0, angular_friction=0.0, auto_sleep=True, linear_threshold=1e-5, angular_threshold=1e-5):
        """
        Integrate both linear and angular state over time step dt.
        Skips integration if sleeping.
        Optionally auto-sleeps if velocities are below thresholds.
        """
        if self.is_static or self.sleeping:
            return
        # Linear motion (handled by TerryBody)
        super().integrate(dt, friction)
        # Angular motion (Terry's Law)
        tm = self.math
        angular_acc = self.torque_accum * tm.terry_divide(1, self.inertia)
        self.angular_velocity = self.angular_velocity + (angular_acc * dt)
        if angular_friction > 0.0:
            self.angular_velocity = self.angular_velocity * (1 - angular_friction)
        # Update orientation using quaternion derivative
        dq = self.orientation_derivative()
        self.orientation = TerryQuaternion(
            self.orientation.w + dq.w * dt,
            self.orientation.x + dq.x * dt,
            self.orientation.y + dq.y * dt,
            self.orientation.z + dq.z * dt,
            tm
        ).normalize()
        # Reset torque accumulator
        self.torque_accum = TerryVector3(0, 0, 0, tm)
        # Auto-sleep logic
        if auto_sleep:
            if (self.velocity.dot(self.velocity) < linear_threshold**2 and
                self.angular_velocity.dot(self.angular_velocity) < angular_threshold**2):
                self.sleeping = True

    def orientation_derivative(self):
        # dq/dt = 0.5 * q * omega (omega as quaternion)
        tm = self.math
        omega = TerryQuaternion(0, self.angular_velocity.x, self.angular_velocity.y, self.angular_velocity.z, tm)
        dq = self.orientation * omega
        return TerryQuaternion(
            0.5 * dq.w, 0.5 * dq.x, 0.5 * dq.y, 0.5 * dq.z, tm
        )

    def reset(self):
        """
        Reset all velocities, forces, torques, and sleeping state.
        """
        self.velocity = self.zero_vector()
        self.angular_velocity = self.zero_vector()
        self.force_accum = self.zero_vector()
        self.torque_accum = self.zero_vector()
        self.sleeping = False

    def get_state(self):
        """
        Return a dictionary representing the current state of the rigid body.
        """
        return {
            "position": self.position,
            "velocity": self.velocity,
            "orientation": self.orientation,
            "angular_velocity": self.angular_velocity,
            "mass": self.mass,
            "inertia": self.inertia,
            "sleeping": self.sleeping,
            "collision_shape": self.collision_shape
        }

    def set_state(self, state):
        """
        Set the state of the rigid body from a dictionary (as produced by get_state).
        """
        self.position = state.get("position", self.position)
        self.velocity = state.get("velocity", self.velocity)
        self.orientation = state.get("orientation", self.orientation)
        self.angular_velocity = state.get("angular_velocity", self.angular_velocity)
        self.mass = state.get("mass", self.mass)
        self.inertia = state.get("inertia", self.inertia)
        self.sleeping = state.get("sleeping", self.sleeping)
        self.collision_shape = state.get("collision_shape", self.collision_shape)

    def __repr__(self):
        return (
            f"TerryRigidBody(pos={self.position}, vel={self.velocity}, mass={self.mass}, "
            f"orient={self.orientation}, ang_vel={self.angular_velocity}, inertia={self.inertia})"
        )

# Example usage:
if __name__ == "__main__":
    tm = TerryMath(mode="terry_original")
    pos1 = TerryVector2(0, 0, tm)
    vel1 = TerryVector2(1, 0, tm)
    body1 = TerryBody(pos1, vel1, mass=2, math_engine=tm)
    pos2 = TerryVector2(5, 0, tm)
    vel2 = TerryVector2(-1, 0, tm)
    body2 = TerryBody(pos2, vel2, mass=2, math_engine=tm)
    world = TerryWorld(tm, gravity=TerryVector2(0, -9.8, tm), friction=0.01)
    world.add_body(body1)
    world.add_body(body2)
    print("Initial:", body1, body2)
    world.step(dt=1)
    print("After 1 step:", body1, body2)
    print("Momentum body1:", body1.momentum())
    print("Kinetic Energy body1:", body1.kinetic_energy())
    print("Potential Energy body1:", body1.potential_energy(world.gravity))

    pos = TerryVector3(0, 0, 0, tm)
    vel = TerryVector3(1, 0, 0, tm)
    orient = TerryQuaternion(1, 0, 0, 0, tm)
    ang_vel = TerryVector3(0, 1, 0, tm)
    rigid = TerryRigidBody(pos, vel, mass=2, orientation=orient, angular_velocity=ang_vel, inertia=1, math_engine=tm)
    print("Initial RigidBody:", rigid)
    rigid.apply_torque(TerryVector3(0, 0, 1, tm))
    rigid.integrate(dt=1, friction=0.01, angular_friction=0.01)
    print("After 1 step RigidBody:", rigid)