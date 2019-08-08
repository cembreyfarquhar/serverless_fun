"use strict";
exports.__esModule = true;
exports["default"] = (function (req, res) {
    var _a = req.body, x = _a.x, y = _a.y;
    res.status(200).json({ result: x + y });
});
