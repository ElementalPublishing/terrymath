from terrymath import TerryMath, TerryVector2, TerryVector3
from terryphysics import TerryBody, TerryWorld, TerryRigidBody

def test_body_apply_force_and_integrate():
    tm = TerryMath()
    pos = TerryVector2(0, 0, tm)
    vel = TerryVector2(1, 0, tm)
    body = TerryBody(pos, vel, mass=2, math_engine=tm)
    body.apply_force(TerryVector2(2, 0, tm))
    body.integrate(dt=1)
    assert body.velocity.x == 3
    assert body.position.x == 3

def test_body_momentum_and_kinetic_energy():
    tm = TerryMath()
    pos = TerryVector2(0, 0, tm)
    vel = TerryVector2(3, 0, tm)
    body = TerryBody(pos, vel, mass=2, math_engine=tm)
    momentum = body.momentum()
    ke = body.kinetic_energy()
    assert momentum.x == 6
    assert ke == 9  # 0.5 * 2 * 9

def test_body_potential_energy():
    tm = TerryMath()
    pos = TerryVector2(0, 10, tm)
    vel = TerryVector2(0, 0, tm)
    body = TerryBody(pos, vel, mass=2, math_engine=tm)
    gravity = TerryVector2(0, -10, tm)
    pe = body.potential_energy(gravity)
    assert isinstance(pe, (int, float))

def test_body_impulse():
    tm = TerryMath()
    pos = TerryVector2(0, 0, tm)
    vel = TerryVector2(0, 0, tm)
    body = TerryBody(pos, vel, mass=2, math_engine=tm)
    body.apply_impulse(TerryVector2(2, 0, tm))
    assert body.velocity.x == 1

def test_body_repr():
    tm = TerryMath()
    pos = TerryVector2(0, 0, tm)
    vel = TerryVector2(1, 0, tm)
    body = TerryBody(pos, vel, mass=2, math_engine=tm)
    assert "TerryBody" in repr(body)

def test_world_add_body_and_step():
    tm = TerryMath()
    world = TerryWorld(math_engine=tm)
    pos = TerryVector2(0, 0, tm)
    vel = TerryVector2(0, 0, tm)
    body = TerryBody(pos, vel, mass=1, math_engine=tm)
    world.add_body(body)
    assert body in world.bodies
    world.step(dt=1)
    assert isinstance(body.position, TerryVector2)

def test_world_apply_gravity():
    tm = TerryMath()
    gravity = TerryVector2(0, -10, tm)
    world = TerryWorld(math_engine=tm, gravity=gravity)
    pos = TerryVector2(0, 0, tm)
    vel = TerryVector2(0, 0, tm)
    body = TerryBody(pos, vel, mass=1, math_engine=tm)
    world.add_body(body)
    world.apply_gravity()
    assert body.force_accum.y == -10

def test_world_elastic_collision():
    tm = TerryMath()
    pos1 = TerryVector2(0, 0, tm)
    vel1 = TerryVector2(1, 0, tm)
    body1 = TerryBody(pos1, vel1, mass=1, math_engine=tm)
    pos2 = TerryVector2(1, 0, tm)
    vel2 = TerryVector2(-1, 0, tm)
    body2 = TerryBody(pos2, vel2, mass=1, math_engine=tm)
    world = TerryWorld(math_engine=tm)
    normal = TerryVector2(1, 0, tm)
    world.elastic_collision(body1, body2, normal)
    assert isinstance(body1.velocity, TerryVector2)
    assert isinstance(body2.velocity, TerryVector2)

def test_rigidbody_angular_motion_and_sleep():
    tm = TerryMath()
    pos = TerryVector3(0, 0, 0, tm)
    vel = TerryVector3(0, 0, 0, tm)
    orient = None
    ang_vel = TerryVector3(0, 1, 0, tm)
    rigid = TerryRigidBody(pos, vel, mass=2, orientation=orient, angular_velocity=ang_vel, inertia=1, math_engine=tm)
    rigid.apply_torque(TerryVector3(0, 0, 1, tm))
    rigid.integrate(dt=1)
    assert rigid.angular_velocity.z != 0
    rigid.set_sleeping(True)
    assert rigid.is_sleeping()
    rigid.wake()
    assert not rigid.is_sleeping()

def test_rigidbody_state_and_reset():
    tm = TerryMath()
    pos = TerryVector3(0, 0, 0, tm)
    vel = TerryVector3(1, 2, 3, tm)
    rigid = TerryRigidBody(pos, vel, mass=2, math_engine=tm)
    state = rigid.get_state()
    rigid.reset()
    assert rigid.velocity.x == 0 and rigid.velocity.y == 0 and rigid.velocity.z == 0
    rigid.set_state(state)
    assert rigid.velocity.x == 1 and rigid.velocity.y == 2 and rigid.velocity.z == 3

def test_rigidbody_repr():
    tm = TerryMath()
    pos = TerryVector3(0, 0, 0, tm)
    vel = TerryVector3(1, 0, 0, tm)
    rigid = TerryRigidBody(pos, vel, mass=2, math_engine=tm)
    assert "TerryRigidBody" in repr(rigid)