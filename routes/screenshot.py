from fastapi import APIRouter, Request, Query
from typing import Optional
from pydantic import BaseModel
from utils.screenshot import (
    async_take_screenshot,
    DEFAULT_VIEWPORT_WIDTH,
    DEFAULT_VIEWPORT_HEIGHT,
    MAX_VIEWPORT_WIDTH,
    MAX_VIEWPORT_HEIGHT,
    MIN_VIEWPORT_WIDTH,
    MIN_VIEWPORT_HEIGHT,
)
from utils.url import URL_REGEX

router = APIRouter()


class Screenshot(BaseModel):
    screenshot: str


@router.get(
    "/screenshot", name="Take Screenshot", description="Take a screenshot of a web page", response_model=Screenshot
)
async def screenshot(
        request: Request,
        url: str = Query("None", regex=URL_REGEX),
        full_page: Optional[bool] = Query(
            True,
            alias="full-page",
            title="Full page",
            description="Screenshot a full scrollable page"
        ),
        browser: Optional[str] = Query(
            "chromium",
            title="Browser Type",
            description="Browser type to use (chromium, firefox or webkit)",
            regex="chromium|firefox|webkit",
        ),
        width: Optional[int] = Query(
            DEFAULT_VIEWPORT_WIDTH,
            title="Viewport Width",
            description="Viewport with in pixels",
            ge=MIN_VIEWPORT_WIDTH,
            le=MAX_VIEWPORT_WIDTH,
        ),
        height: Optional[int] = Query(
            DEFAULT_VIEWPORT_HEIGHT,
            title="Viewport Height",
            description="Viewport height in pixels",
            ge=MIN_VIEWPORT_HEIGHT,
            le=MAX_VIEWPORT_HEIGHT,
        )
):
    filename = await async_take_screenshot(url, full_page, browser, width, height)

    return {
        "screenshot": request.url_for("screenshots", path=f"/{filename}"),
    }
