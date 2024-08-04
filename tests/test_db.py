from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='Test User2',
        email='testuser2@server.com',
        password='usertestpwd',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'testuser2@server.com')
    )

    assert result.username == 'Test User2'
