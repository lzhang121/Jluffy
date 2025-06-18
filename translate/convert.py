

from playwright.sync_api import sync_playwright


def html_to_pdf(input_path, output_path):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(input_path)
        page.pdf(path=output_path)
        browser.close()


html_to_pdf("https://www.yahoo.co.jp",
            "output_with_furigana.pdf")
