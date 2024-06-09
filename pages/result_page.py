from selene.support.shared import browser
from selene import have


class ResultPage:

    def should_have_text(self, text):
        browser.element('.table-responsive').should(have.text(text))
        return self

    def should_have_hobbies(self, hobbies):
        for hobby in hobbies:
            browser.element('.table-responsive').should(have.text(hobby))
        return self

    def close(self):
        browser.element('#closeLargeModal').click()
        return self
