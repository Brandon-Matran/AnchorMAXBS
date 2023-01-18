from fastapi import APIRouter, Depends, Response, HTTPException, status
from typing import Union, List, Optional

# from token_auth import get_current_user
from auth import authenticator
from queries.listings import (
    ListingError,
    ListingIn,
    ListingRepository,
    ListingOut,
)

router = APIRouter()

# not_authorized = HTTPException(
#     status_code=status.HTTP_401_UNAUTHORIZED,
#     detail="Invalid authentication credentials",
#     headers={"WWW-Authenticate": "Bearer"},
# )


@router.get("/listings", response_model=Union[List[ListingOut], ListingError])
def all_listings(
    repo: ListingRepository = Depends(),
):
    return repo.all_listings()


@router.post("/listings", response_model=Union[ListingOut, ListingError])
def create_listing(
    listing: ListingIn,
    response: Response,
    repo: ListingRepository = Depends(),
    # account: dict = Depends(get_current_user),
    account: dict = Depends(authenticator.get_current_account_data),
):
    # if "company" not in account.user_type:
    #     raise not_authorized
    # return repo.create(listing)
    if account["user_type"] == "company":
        return repo.create(listing)
    else:
        raise HTTPException(
            status_code=401, detail="Only company user can post job listing"
        )


@router.delete("/listings/{listing_id}", response_model=bool)
def delete_listing(
    listing_id: int,
    repo: ListingRepository = Depends(),
    # account: dict = Depends(get_current_user),
    account: dict = Depends(authenticator.get_current_account_data),
) -> bool:
    if account["user_type"] == "company":
        return repo.delete(listing_id)
    else:
        raise HTTPException(
            status_code=401, detail="Only company user can delete job listing"
        )


@router.put("/listings/{listing_id}", response_model=ListingOut)
def update_listing(
    listing_id: int,
    listing: ListingIn,
    repo: ListingRepository = Depends(),
    account: dict = Depends(authenticator.get_current_account_data),
) -> ListingOut:
    if account["user_type"] == "company":
        return repo.update(listing_id, listing)
    else:
        raise HTTPException(
            status_code=401, detail="Only company user can update job listing"
        )


@router.get("/listings/{listing_id}", response_model=Optional[ListingOut])
def get_one_listing(
    listing_id: int,
    response: Response,
    repo: ListingRepository = Depends(),
) -> ListingOut:
    listing = repo.get_one(listing_id)
    if listing is None:
        response.status_code = 404
    return listing
