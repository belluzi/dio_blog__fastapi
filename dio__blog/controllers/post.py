from fastapi import APIRouter, Depends, Response, status
from ..schemas.post import PostIn, PostUpdate
from ..security import login_required
from ..services import post as service
from ..views.post import PostOut

router = APIRouter(prefix="/posts", dependencies=[Depends(login_required)])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    return await service.create_post(post)


@router.get("/", response_model=list[PostOut])
async def read_posts(published: bool | None = None, limit: int = 10, skip: int = 0):
    return await service.read_all(published=published, limit=limit, skip=skip)


@router.patch("/{post_id}", status_code=status.HTTP_200_OK, response_model=PostOut)
async def update_post(post_id: int, data: PostUpdate):
    return await service.update_post(post_id, data)


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    await service.delete_post(post_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
