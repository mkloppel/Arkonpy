class ScrollableFrameMixin:
    def add_scroll_functionality(self, canvas):
        canvas.bind_all("<MouseWheel>", lambda e: self._on_mousewheel(e, canvas))
        
    def _on_mousewheel(self, event, canvas):
        x, y = canvas.winfo_pointerxy()
        widget_under_mouse = canvas.winfo_containing(x, y)
        
        if widget_under_mouse and (canvas is widget_under_mouse or canvas in widget_under_mouse.winfo_parents()):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
