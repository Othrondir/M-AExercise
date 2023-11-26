from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class MyTestClas(BaseCase):
    def test(self):
        selectores = ['//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/span/div/div/div[1]/span/a/div/img', '//*[@id="newAccordionRow_1"]/div/div[1]/i']
        # Step 1: Go to https://www.amazon.com
        self.open("https://www.amazon.com/")
        # Step 2: Search for "hats for men" 
        self.type("input#twotabsearchtextbox", "hats for men\n")
        self.click_xpath('/html/body/div[1]/div[1]/span[2]/div/h1/div/div[4]/div/div/form/span/span/span/span')
        self.click_xpath('/html/body/div[4]/div/div/ul/li[2]/a')
        self.click_xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div/div/div[1]/span/a/div/img')
        # Step 3: Add first hat to Cart with quantity 2
        self.click_xpath('/html/body/div[1]/div[1]/div/div[7]/div[1]/div[2]/div[2]/div/div/div[2]/div[4]/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[10]/div/div/span/div/div/span/span/span')
        self.click("a#quantity_1")
        self.click("input#add-to-cart-button")                    
        # Step 4: Open cart and assert total price and quantity are correct
        self.click_xpath('//*[@id="sw-gtc"]/span/a')
        self.assert_text("Subtotal (2 items):", "#sc-subtotal-label-buybox")
        # Step 5: Search for "hats for women"
        self.type("input#twotabsearchtextbox", "hats for women\n")
        self.click_xpath('/html/body/div[1]/div[1]/span[2]/div/h1/div/div[4]/div/div/form/span/span/span/span')
        self.click_xpath('/html/body/div[4]/div/div/ul/li[2]/a')
        self.click_xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div/div/div[1]/span/a/div/img')
        # Step 6: Add first hat to Cart with quantity 1
        self.click("input#add-to-cart-button") 
        # Step 7: Open cart and assert total price and quantity are correct
        self.click_xpath('//*[@id="sw-gtc"]/span/a')
        self.assert_text("Subtotal (3 items):", "#sc-subtotal-label-buybox")
        # Step 8: Change the quantity for item selected at step 3 from 2 to 1 item in Cart
        self.click_xpath('/html/body/div[1]/div[1]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[4]/div[4]/div/div[2]/div[1]/span[1]/span/span[1]/span/span/span/span')
        self.click("a#quantity_1")
        # Step 9: Assert total price and quantity are changed correctly
        element_1 = self.find_element('/html/body/div[1]/div[1]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[2]/ul/div[1]/div/div[1]/div/span')
        element_2 = self.find_element('/html/body/div[1]/div[1]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[4]/div[4]/div/div[2]/ul/div[1]/div/div/div/span')
        number1 = float(element_1.text.replace('$', ''))
        number2 = float(element_2.text.replace('$', ''))
        sum = round(number1 + number2, 2)
        self.sleep(3)
        element_number_verification = self.find_element('//*[@id="sc-subtotal-amount-activecart"]')
        number_verification = float(element_number_verification.text.replace('$', ''))
        assert sum == number_verification, f"Total price ({sum}) changed incorrectly ({number_verification})"
        self.assert_text("Subtotal (2 items):", "#sc-subtotal-label-buybox")
