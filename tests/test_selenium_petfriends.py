import time
# from settings import valid_email, valid_password

def test_petfriends(selenium):
    # Open PetFriends base page:
    selenium.get("https://petfriends1.herokuapp.com/")
    time.sleep(3)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = selenium.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()

    # click existing user button
    btn_exist_acc = selenium.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = selenium.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys("test227@gmail.com")

    # add password
    field_pass = selenium.find_element_by_id("pass")
    field_pass.clear()
    field_pass.send_keys("test227")

    # click submit button
    btn_submit = selenium.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()
    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # click my pets
    # если ширина окна < 800
    # btn_navbar = selenium.find_element_by_class_name("navbar-toggler-icon")
    # btn_navbar.click()
    # time.sleep(3)  # just for demo purposes, do NOT repeat it on real projects!
    btn_my_pets = selenium.find_element_by_xpath("//a[@href='/my_pets']")
    btn_my_pets.click()
    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    if selenium.current_url == 'https://petfriends1.herokuapp.com/my_pets':
        # Make the screenshot of browser window:
        selenium.save_screenshot('result_my_pets.png')
    else:
        raise Exception("login error")

    # click logout
    btn_logout = selenium.find_element_by_xpath("//button[@class='btn btn-outline-secondary']")
    btn_logout.click()
    time.sleep(5)