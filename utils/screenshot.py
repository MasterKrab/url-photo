from uuid import uuid4
from playwright.async_api import async_playwright
from utils.user_agent import get_random_user_agent

DEFAULT_VIEWPORT_WIDTH = 1920
DEFAULT_VIEWPORT_HEIGHT = 1080
MAX_VIEWPORT_WIDTH = 3000
MAX_VIEWPORT_HEIGHT = 3000
MIN_VIEWPORT_WIDTH = 320
MIN_VIEWPORT_HEIGHT = 300


def get_filename():
    return f"screenshot-{uuid4()}.png"


async def async_take_screenshot(
        url, full_page, browser_type, width=DEFAULT_VIEWPORT_WIDTH, height=DEFAULT_VIEWPORT_HEIGHT
):
    async with async_playwright() as playwright:
        browser = await getattr(playwright, browser_type).launch(headless=browser_type == "firefox")

        context = await browser.new_context(
            viewport={"width": width, "height": height},
            extra_http_headers={"User-Agent": get_random_user_agent()},
            locale="en",
            ignore_https_errors=True,
        )

        page = await context.new_page()
        await page.goto(url, timeout=10000)

        filename = get_filename()
        await page.screenshot(path=f"screenshots/{filename}", full_page=full_page)

        await browser.close()

        return filename
