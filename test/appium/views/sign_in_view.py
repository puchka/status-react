from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from tests import common_password
from views.base_element import BaseButton, BaseEditBox, BaseText
from views.base_view import BaseView

class MultiAccountButton(BaseButton):
    class Username(BaseText):
        def __init__(self, driver, locator_value):
            super(MultiAccountButton.Username, self).__init__(driver)
            self.locator = self.Locator.xpath_selector(locator_value + '/android.view.ViewGroup/android.widget.TextView[1]')

    def __init__(self, driver, position=1):
        super(MultiAccountButton, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//*[@content-desc='select-account-button-%s']" % position)
        self.username = self.Username(driver, self.locator.value)


class MultiAccountOnLoginButton(BaseButton):
    def __init__(self, driver, position=1):
        super(MultiAccountOnLoginButton, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("(//*[@content-desc='chat-icon'])[%s]/.." % position)


class PasswordInput(BaseEditBox):
    def __init__(self, driver):
        super(PasswordInput, self).__init__(driver)
        self.locator = self.Locator.accessibility_id("password-input")


class RecoverAccountPasswordInput(BaseEditBox):
    def __init__(self, driver):
        super(RecoverAccountPasswordInput, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//android.widget.TextView[@text='Password']"
                                                   "/following-sibling::android.view.ViewGroup/android.widget.EditText")


class CreatePasswordInput(BaseEditBox):
    def __init__(self, driver):
        super(CreatePasswordInput, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//android.widget.TextView[@text='Create a password']/.."
                                                   "//android.widget.EditText")


class ConfirmYourPasswordInput(BaseEditBox):
    def __init__(self, driver):
        super(ConfirmYourPasswordInput, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//android.widget.TextView[@text='Confirm your password']/.."
                                                   "//android.widget.EditText")


class SignInButton(BaseButton):

    def __init__(self, driver):
        super(SignInButton, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//android.widget.TextView[@text='Sign in' or @text='Submit']")

    def navigate(self):
        from views.home_view import HomeView
        return HomeView(self.driver)


class LetsGoButton(BaseButton):
    def __init__(self, driver):
        super(LetsGoButton, self).__init__(driver)
        self.locator = self.Locator.accessibility_id('lets-go-button')


class RecoverAccessButton(BaseButton):

    def __init__(self, driver):
        super(RecoverAccessButton, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//android.widget.TextView[@text='Recover access']")

    def navigate(self):
        from views.recover_access_view import RecoverAccessView
        return RecoverAccessView(self.driver)

class KeycardKeyStorageButton(BaseButton):

    def __init__(self, driver):
        super(KeycardKeyStorageButton, self).__init__(driver)
        self.locator = self.Locator.accessibility_id("select-storage-:advanced")

    def navigate(self):
        from views.keycard_view import KeycardView
        return KeycardView(self.driver)

    def click(self):
        self.scroll_to_element().click()
        return self.navigate()



class CreateMultiaccountButton(BaseButton):
    def __init__(self, driver):
        super(CreateMultiaccountButton, self).__init__(driver)
        self.locator = self.Locator.xpath_selector(
            "//*[@text='Create multiaccount' or @text='Create new multiaccount']")


class YourKeysMoreIcon(BaseButton):
    def __init__(self, driver):
        super(YourKeysMoreIcon, self).__init__(driver)
        self.locator = self.Locator.accessibility_id("your-keys-more-icon")


class GenerateKeyButton(BaseButton):
    def __init__(self, driver):
        super(GenerateKeyButton, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//*[@text='Generate keys']")


class GenerateNewKeyButton(BaseButton):
    def __init__(self, driver):
        super(GenerateNewKeyButton, self).__init__(driver)
        self.locator = self.Locator.accessibility_id('generate-a-new-key')


class IHaveMultiaccountButton(RecoverAccessButton):
    def __init__(self, driver):
        super(IHaveMultiaccountButton, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//*[@text='I already have a multiaccount']")


class AccessKeyButton(RecoverAccessButton):
    def __init__(self, driver):
        super(AccessKeyButton, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//*[@text='Access key']")


class MaybeLaterButton(BaseButton):
    def __init__(self, driver):
        super(MaybeLaterButton, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//*[@text='Maybe later']")


class AddExistingMultiaccountButton(RecoverAccessButton):
    def __init__(self, driver):
        super(AddExistingMultiaccountButton, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//*[@text='Add existing multiaccount']")


class ConfirmPasswordInput(BaseEditBox):
    def __init__(self, driver):
        super(ConfirmPasswordInput, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//android.widget.TextView[@text='Confirm']"
                                                   "/following-sibling::android.view.ViewGroup/android.widget.EditText")


class NameInput(BaseEditBox):
    def __init__(self, driver):
        super(NameInput, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//android.widget.EditText")


class OtherMultiAccountsButton(BaseButton):

    def __init__(self, driver):
        super(OtherMultiAccountsButton, self).__init__(driver)
        self.locator = self.Locator.text_selector('Other multiaccounts')


class PrivacyPolicyLink(BaseButton):
    def __init__(self, driver):
        super(PrivacyPolicyLink, self).__init__(driver)
        self.locator = self.Locator.text_part_selector('privacy policy')

    def click(self):
        element = self.find_element()
        location = element.location
        size = element.size
        x = int(location['x'] + size['width'] * 0.9)
        y = int(location['y'] + size['height'] * 0.8)
        TouchAction(self.driver).tap(None, x, y).perform()
        self.driver.info('Tap on %s' % self.name)
        return self.navigate()

    def navigate(self):
        from views.web_views.base_web_view import BaseWebView
        return BaseWebView(self.driver)


class SignInView(BaseView):

    def __init__(self, driver, skip_popups=True):
        super(SignInView, self).__init__(driver)
        self.driver = driver
        if skip_popups:
            self.accept_agreements()

        self.password_input = PasswordInput(self.driver)
        self.recover_account_password_input = RecoverAccountPasswordInput(self.driver)

        self.sign_in_button = SignInButton(self.driver)
        self.recover_access_button = RecoverAccessButton(self.driver)

        # new design
        self.create_multiaccount_button = CreateMultiaccountButton(self.driver)
        self.i_have_multiaccount_button = IHaveMultiaccountButton(self.driver)
        self.access_key_button = AccessKeyButton(self.driver)
        self.generate_key_button = GenerateKeyButton(self.driver)
        self.your_keys_more_icon = YourKeysMoreIcon(self.driver)
        self.generate_new_key_button = GenerateNewKeyButton(self.driver)
        self.add_existing_multiaccount_button = AddExistingMultiaccountButton(self.driver)
        self.confirm_password_input = ConfirmPasswordInput(self.driver)
        self.create_password_input = CreatePasswordInput(self.driver)
        self.confirm_your_password_input = ConfirmYourPasswordInput(self.driver)
        self.maybe_later_button = MaybeLaterButton(self.driver)
        self.name_input = NameInput(self.driver)
        self.other_multiaccounts_button = OtherMultiAccountsButton(self.driver)
        self.multiaccount_button = MultiAccountButton(self.driver)
        self.multi_account_on_login_button = MultiAccountOnLoginButton(self.driver)
        self.privacy_policy_link = PrivacyPolicyLink(self.driver)
        self.lets_go_button = LetsGoButton(self.driver)
        self.keycard_storage_button = KeycardKeyStorageButton(self.driver)

    def create_user(self, password=common_password, keycard=False):
        self.get_started_button.click()
        self.generate_key_button.click()
        self.next_button.click()
        if keycard:
            keycard_flow = self.keycard_storage_button.click()
            self.next_button.click()
            keycard_flow.begin_setup_button.click()
            keycard_flow.connect_card_button.click()
            keycard_flow.enter_default_pin()
            keycard_flow.enter_default_pin()
            self.next_button.scroll_to_element()
            self.next_button.wait_for_visibility_of_element(20)
            self.next_button.click()
            self.yes_button.click()
            keycard_flow.backup_seed_phrase()
        else:
            self.next_button.click()
            self.create_password_input.set_value(password)
            self.next_button.click()
            self.confirm_your_password_input.set_value(password)
            self.next_button.click()
        self.lets_go_button.wait_for_visibility_of_element(30)
        self.lets_go_button.click_until_absense_of_element(self.lets_go_button)
        self.profile_button.wait_for_visibility_of_element(30)
        return self.get_home_view()

    def recover_access(self, passphrase: str, password: str = common_password):
        recover_access_view = self.access_key_button.click()
        recover_access_view.enter_seed_phrase_button.click()
        recover_access_view.seedphrase_input.click()
        recover_access_view.seedphrase_input.set_value(passphrase)
        recover_access_view.next_button.click()
        recover_access_view.reencrypt_your_key_button.click()
        recover_access_view.next_button.click()
        recover_access_view.create_password_input.set_value(password)
        recover_access_view.next_button.click()
        recover_access_view.confirm_your_password_input.set_value(password)
        recover_access_view.next_button.click_until_presence_of_element(self.lets_go_button)
        self.lets_go_button.click()
        self.profile_button.wait_for_visibility_of_element(30)
        return self.get_home_view()

    def sign_in(self, password=common_password, keycard=False):
        self.rooted_device_continue()
        self.multi_account_on_login_button.wait_for_visibility_of_element(5)
        self.multi_account_on_login_button.click()
        if keycard:
            from views.keycard_view import KeycardView
            keycard_view = KeycardView(self.driver)
            keycard_view.enter_default_pin()
            keycard_view.connect_card_button.click()
        else:
            self.password_input.set_value(password)
            self.sign_in_button.click()
        return self.get_home_view()

    def get_account_by_position(self, position: int):
        account_button = MultiAccountButton(self.driver, position)
        if account_button.is_element_displayed():
            return account_button
        else:
            raise NoSuchElementException(
                'Device %s: Unable to find multiaccount by position %s' % (self.driver.number, position)) from None

    def open_weblink_and_login(self, url_weblink):
        self.open_universal_web_link(url_weblink)
        self.sign_in()
