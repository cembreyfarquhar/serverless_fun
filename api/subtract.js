module.exports = (req, res) => {
    const { x, y } = req.body
    res.status(200).json({ result: x - y })
}
