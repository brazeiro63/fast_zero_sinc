from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='brazeiro',
        email='user@server.com',
        password='umaSenhaDificil',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'user@server.com')
    )

    assert result.username == 'brazeiro'
