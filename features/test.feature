Feature: Arts & Crafts Department


  Scenario Outline: Selecting from Engraving Machines & Tools
    When user navigates to Amazon website in "<browser>"
    Then Amazon web page is displayed
    When user clicks on All_Hamburger_Menu
    And user clicks on Arts_And_Crafts_Menu
    And user clicks on Beading_And_Jewelry_Making_Menu
    And user clicks on Arts_Crafts_And_Sewing_Menu
    And user clicks on Beading_And_Jewelry_Making
    And user clicks on Jewelry_Making_Engraving_Machines_And_Tools
    And user clicks on Sort_By_Dropdown_Button
    And user cliks on Price_High_To_Low
    And user clicks on Third_Product_Of_Engraving_Machines_And_Tools
    Then user checks the review score for the selected product
    Then user checks the price for the selected product
    Examples:
      |browser  |
      |chrome   |
      #|headless |
