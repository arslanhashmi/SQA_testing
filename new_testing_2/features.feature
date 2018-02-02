

# features for automation assingment

Feature: Passing parameter to steps

  Scenario: check the login page is opened

    Given I have to open "http://www.phptravels.net/"
    When I find and click on "/html/body/div[@class='navbar navbar-static-top navbar-default ']/div[@class='container']/div[@class='navbar']/div[@class='navbar-collapse collapse']/ul[@class='nav navbar-nav navbar-right currency_btn']/ul[@class='nav navbar-nav navbar-side navbar-right sidebar']/li[@id='li_myaccount']/a[@class='dropdown-toggle go-text-right']" button
    And I find and click on "/html/body/div[@class='navbar navbar-static-top navbar-default ']/div[@class='container']/div[@class='navbar']/div[@class='navbar-collapse collapse']/ul[@class='nav navbar-nav navbar-right currency_btn']/ul[@class='nav navbar-nav navbar-side navbar-right sidebar']/li[@id='li_myaccount']/ul[@class='dropdown-menu']/li[1]/a[@class='go-text-right']" button
    Then I wait for "3" sec

  Scenario: login to the application

    Given I assert "http://www.phptravels.net/login" page should be opened
    When I enter "user@phptravels.com" in "//*[@id="loginfrm"]/div[1]/div[5]/div/div[1]/input" field
    And I enter "demouser" in "//*[@id="loginfrm"]/div[1]/div[5]/div/div[2]/input" field
    When I find and click on "//*[@id="loginfrm"]/div[1]/div[5]/button" button
    Then I wait for "5" sec
    And I assert "http://www.phptravels.net/account/" page should be opened
    And I assert "Hi" is here in "//h3[@class="RTL"]"

  Scenario: Edit information

    Given I find and click on "//*[@id="body-section"]/div/div[3]/div/div[1]/ul/li[2]" button
    When I enter "RANDOM-STRING-LENGTH:10" in "firstname" readonly field
    And I enter "RANDOM-STRING-LENGTH:10" in "lastname" readonly field
    When I enter "RANDOM-STRING-LENGTH:100" in "//*[@id="profilefrm"]/div/div[3]/div[2]/div[1]/div[2]/input" field
    And I enter "Lahore" in "//*[@id="profilefrm"]/div/div[3]/div[2]/div[3]/div[2]/input" field
    And I enter "Punjab" in "//*[@id="profilefrm"]/div/div[3]/div[2]/div[4]/div[2]/input" field
    And I enter "54000" in "//*[@id="profilefrm"]/div/div[3]/div[2]/div[5]/div[2]/input" field
    And I select "Pakistan" in "country" dropdown
    And I find and click on "//*[@id="profilefrm"]/div/div[3]/div[3]/button" button
    Then I wait for "1" sec
    And I assert "Profile Updated Successfully." is here in "//*[@id="profile"]/div[2]/div[2]/div"

  Scenario: Send message from contact page

    Given I find and click on "/html/body/nav[1]/div/div/div/ul/li[6]" button
    When I enter "RANDOM-STRING-LENGTH:10" in "//input[@placeholder="Name"]" field
    And I enter "RANDOM-STRING-EMAIL-LENGTH:10" in "//input[@placeholder="Email"]" field
    And I enter "Hello World" in "//input[@placeholder="Subject"]" field
    And I enter "RANDOM-STRING-LENGTH:100" in "//textarea[@placeholder="Message"]" field
    When I find and click on "//input[@name="submit_contact"]" button
    Then I wait for "1" sec
    And I assert "Message Sent Successfully" is here in "//*[@id="body-section"]/div[1]/div/div/div/form/div[1]/div[1]"


  Scenario: Logout
    
    Given I find and click on "sidebar" button "1" in class list
    When I find and click on "dropdown-menu" anchor "1" in "3" number search by class
    Then I assert "http://www.phptravels.net/login" page should be opened
    


