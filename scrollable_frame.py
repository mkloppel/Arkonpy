class ScrollableFrameMixin:
    def add_scroll_functionality(self, canvas):
        canvas.bind_all("<MouseWheel>", lambda e: self._on_mousewheel(e, canvas))
        
    def _on_mousewheel(self, event, canvas):
        x, y = canvas.winfo_pointerxy()
        widget_under_mouse = canvas.winfo_containing(x, y)
        
        # Check if widget_under_mouse is the canvas or a child of it
        parent = widget_under_mouse
        while parent:
            if parent == canvas:
                canvas.yview_scroll(int(-1*(event.delta/120)), "units")
                break
            parent = parent.master if hasattr(parent, 'master') else None
