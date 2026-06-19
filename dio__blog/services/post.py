from fastapi import HTTPException, status
from ..database import database
from ..models.post import posts
from ..schemas.post import PostIn, PostUpdate
from databases.interfaces import Record


async def create_post(post: PostIn) -> Record:
    command = posts.insert().values(
        title = post.title,
        content = post.content,
        published_at = post.date,
        published = post.published,
    )

    last_id = await database.execute(command)

    return await get_post(last_id)


async def read_all(published: bool | None = None, limit: int = 10, skip: int = 0) -> list[Record]:
    query = posts.select()

    if published is not None:
        query = query.where(posts.c.published == published)

    query = query.offset(skip).limit(limit)
    return await database.fetch_all(query)


async def update_post(post_id: int, data: PostUpdate) -> Record:
    await get_post(post_id)

    update_data = data.model_dump(exclude_unset=True)

    if update_data:
        command = posts.update().where(posts.c.id == post_id).values(**update_data)
        await database.execute(command)

    return await get_post(post_id)


async def delete_post(post_id: int) -> None:
    await get_post(post_id)

    command = posts.delete().where(posts.c.id == post_id)
    await database.execute(command)


async def get_post(post_id: int) -> Record:
    query = posts.select().where(posts.c.id == post_id)
    post = await database.fetch_one(query)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )

    return post
