from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from datetime import date
from dateutil import relativedelta

class MainApp(App):
    def build(self):
        self.icon = 'icon.png'
        layout = BoxLayout(orientation='vertical', padding = (0,0,0,900), spacing = 1)
        self.heading = Label(text='Compound Interest Calculator', size_hint=(1,.2))
        layout.add_widget(self.heading)
        self.principalheading = Label(text='Enter Principal', size_hint=(1,.2))
        layout.add_widget(self.principalheading)
        self.principal = TextInput(multiline=False, size_hint= (1, .1), input_type = 'number', input_filter='float')
        layout.add_widget(self.principal)
        self.startheading = Label(text='Enter Start Date in DD/MM/YYYY', size_hint=(1, .2))
        layout.add_widget(self.startheading)
        self.start = TextInput(multiline=False, size_hint= (1, .1), input_type = 'number')
        layout.add_widget(self.start)
        self.endheading = Label(text='Enter End Date in DD/MM/YYYY', size_hint=(1, .2))
        layout.add_widget(self.endheading)
        self.end = TextInput(multiline=False, size_hint= (1, .1), input_type = 'number')
        layout.add_widget(self.end)
        self.rateheading = Label(text='Enter Rate of Interest in Rupees \n  (Divide it by 12 if it is in %)', size_hint=(1, .2))
        layout.add_widget(self.rateheading)
        self.rate = TextInput(multiline=False, size_hint= (1, .1), input_filter = 'float', input_type = 'number')
        layout.add_widget(self.rate)
        self.btn = Button(text = 'Calculate', size_hint= (1, .17))
        self.btn.bind(on_press=self.show)
        layout.add_widget(self.btn)
        return layout

    def show(self,btn):
        layout = BoxLayout(orientation='vertical')
        try:
            duration,interest,Amount = self.program(self.principal,self.start,self.end,self.rate)
            popupLabel = Label(text=str(duration.years)+" Years "+str(duration.months)+" Months "+str(duration.days)+" Days \n""Interest : "+"  "+str(interest)+"\nAmount : "+"  "+str(Amount))
            layout.add_widget(popupLabel)
        except:
            label = Label(text = 'Enter Valid Input')
            layout.add_widget(label)
        closeButton = Button(text="Close Window", size_hint= (.45, .1))
        layout.add_widget(closeButton)
        popup = Popup(title='Amount', content=layout)
        popup.open()
        closeButton.bind(on_press=popup.dismiss)

    def program(self,principal,start,end,rate):
        p = principal.text
        t1 = start.text
        t2 = end.text
        r = rate.text
        d1 = date(int(t1[6:10]), int(t1[3:5]), int(t1[0:2]))
        d2 = date(int(t2[6:10]), int(t2[3:5]), int(t2[0:2]))
        number = d2 - d1
        dur = relativedelta.relativedelta(d2, d1)
        p = int(p)
        t = number.days
        r = float(r)
        i1 = 0
        while (t > 365):
            i = p * r * 365 / 3000
            i1 = i1 + i
            p = p + i
            t = t - 365
        i = p * r * t / 3000
        i1 = i1 + i
        A = p + i
        return dur,i1,A


MainApp().run()