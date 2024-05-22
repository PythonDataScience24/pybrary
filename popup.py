import gooeypie as gp


class Popup:
    @staticmethod
    def show_error(message):
        popup = gp.GooeyPieApp('Error')
        popup.set_grid(3, 1)

        msg = gp.Label(popup, message)
        msg.align = 'center'
        popup.add(msg, 1, 1, align='center')

        okay_btn = gp.Button(popup, 'Okay', lambda event: popup.destroy())
        popup.add(okay_btn, 3, 1, align='right')

        popup.run()
