Feature: Order status notification

  Scenario: The order becomes ready → the client receives a notification
    Given An order with ID "Drink-001" was created
    And client "TestClient" subscribed to notifications
    When the order status changes to "ready"
    Then "TestClient" should see the message: "TestClient, order Drink-001: ready!"