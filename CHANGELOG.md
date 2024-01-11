# Change Log

## v 1.1.0

**Improved/fixed how tkinter methods are applied to tkVFD display objects, which now respond the same as any other tkinter canvas object.**

Previously tkinter methods had to be applied when either using <code>.control()</code> or <code>.char()</code> as this was when the canvas object was apparent. For example:

```
disp = tkVFD.seg7(root, height=200)
disp.char('8').pack(side=tk.LEFT)
```

Now a ```__getattr__``` function has been defined which looks at the tkinter package for all methods not native to tkVFD. Thus tkinter methods can be applied at any time. For example:

```
disp = tkVFD.seg7(root, height=200)
disp.char('8')
disp.pack(side=tk.LEFT)
```

## v 1.0.0 (Jan 4, 2024)

Initial tkVFD release.
