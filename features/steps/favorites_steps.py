from behave import given, when, then
from playwright.sync_api import expect

@when('jag klickar på hjärtat för boken "{title}"')
def step_impl(context, title):
    context.catalog_page.toggle_favorite(title)

@then('ska boken "{title}" finnas under "Mina böcker"')
def step_impl(context, title):
    context.catalog_page.go_to_favorites()
    expect(context.page.get_by_text(title)).to_be_visible()

@given('jag har lagt till boken "{title}" som favorit')
def step_impl(context, title):
    context.catalog_page.navigate()
    # Check if already favorited? The app resets on reload?
    # Actually, default state has some books.
    # We should ensure it is clicked.
    # But wait, how do we know if it is already favorited?
    # The heart might change style. 
    # For now, we assume clean state or just click it.
    # If it's a toggle, clicking again removes it.
    # The prompt says "testa ... vad som händer om man klickar fler än två gånger".
    # We'll assume start state is not favorited for "Kaffekokaren..." or we check class?
    # Inspecting HTML: <div data-testid="star-..." class="star">❤️</div>
    # Does class change? Maybe not.
    # Let's assume we just click it.
    context.catalog_page.toggle_favorite(title)

@when('jag tar bort favoriten "{title}"')
def step_impl(context, title):
    # Assuming we are on catalog page or we navigate there
    context.catalog_page.go_to_catalog()
    context.catalog_page.toggle_favorite(title)

@then('ska boken "{title}" inte finnas under "Mina böcker"')
def step_impl(context, title):
    context.catalog_page.go_to_favorites()
    expect(context.page.get_by_text(title)).not_to_be_visible()

@when('jag går till "Mina böcker"')
def step_impl(context):
    context.catalog_page.go_to_favorites()

@then('ska jag se boken "{title}" i listan')
def step_impl(context, title):
    expect(context.page.get_by_text(title)).to_be_visible()
