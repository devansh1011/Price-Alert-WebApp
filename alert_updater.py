from models.alert import Alert

alerts = Alert.all()

for alert in alerts:
    alert.load_item_price()

if not alerts:
    print("No alerts have been created. Add an item and an alert to begin!")