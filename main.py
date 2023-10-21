from kivy.app import App
from kivy.uix.button import Button
import pydroid
from androidintent import Intent

class MediaStorageRefreshApp(App):

    def build(self):
        # Создаем кнопку, которая будет выполнять код при нажатии
        button = Button(text='Обновить медиа-хранилище')
        button.bind(on_press=self.refresh_media_storage)
        return button

    def refresh_media_storage(self, instance):
        # Создаем объект Pydroid
        droid = pydroid.create_droid()

        # Отправляем намеренный участок кода для обновления медиа-хранилища
        intent = Intent()
        intent.set_action("android.intent.action.MEDIA_MOUNTED")
        intent.set_data("file:///sdcard/")
        droid.send_intent(intent)

        # Закрываем Pydroid
        droid.close()

if __name__ == '__main__':
    MediaStorageRefreshApp().run()
