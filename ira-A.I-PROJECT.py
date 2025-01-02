import kivy from kivy.app import App from kivy.uix.boxlayout import BoxLayout from kivy.uix.label import Label from kivy.uix.button import Button from kivy.uix.textinput import TextInput kivy.require('2.0.0')
class CoffeeShopChatbotApp(App): def build(self):
self.menu = {
"coffee": 3.00,
"tea": 2.50,
"hot chocolate": 3.50,
"sandwiches": 5.00,
"salads": 4.50
}
self.order = {} layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
self.result_label = Label(text="Welcome to our cafe!") layout.add_widget(self.result_label)
self.order_input = TextInput(hint_text='Enter item (coffee, tea, etc.)', multiline=False) layout.add_widget(self.order_input)
self.quantity_input = TextInput(hint_text='Enter quantity', multiline=False) layout.add_widget(self.quantity_input)
add_button = Button(text='Add to Order') add_button.bind(on_press=self.add_to_order) layout.add_widget(add_button)
finalize_button = Button(text='Finalize Order') finalize_button.bind(on_press=self.finalize_order) layout.add_widget(finalize_button)
info_button = Button(text='Show Cafe Info') info_button.bind(on_press=self.show_info) layout.add_widget(info_button) return layout
def add_to_order(self, instance): item = self.order_input.text.lower() quantity_text = self.quantity_input.text
if item in self.menu: try:
quantity = int(quantity_text) if quantity > 0:
self.order[item] = self.order.get(item, 0) + quantity self.result_label.text = f"Added {quantity} x {item} to order."
else:
self.result_label.text = "Please enter a valid quantity."
except ValueError:
self.result_label.text = "Please enter a valid number for quantity."
else: self.result_label.text = "Item not on the menu."
# Clear input fields self.order_input.text = '' self.quantity_input.text = ''
def finalize_order(self, instance):
if not self.order:
self.result_label.text = "No items ordered." return
total = sum(self.menu[item] * quantity for item, quantity in self.order.items()) order_summary = "Your order:n"
for item, quantity in self.order.items():
order_summary += f"{quantity} x {item}n" order_summary += f"Total: ${total:.2f}" self.result_label.text = order_summary
def show_info(self, instance): cafe_info = {
"hours": "8am - 6pm",
"location": "cafe insiders"
}
info_message = f"Hours: {cafe_info['hours']}nLocation: {cafe_info['location']}" self.result_label.text = info_message
if __name__ == '__main__':
CoffeeShopChatbotApp().run()
#SD
