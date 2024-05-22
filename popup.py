import gooeypie as gp


class Popup:
    @staticmethod
    def show_error(message):
        popup = gp.GooeyPieApp('Error')
        popup.set_grid(3, 1)

        msg = gp.Label(popup, message)
        msg.align = 'center'
        popup.add(msg, 1, 1, align='center')

        popup.run()
