module.exports = (req, res) => {
    const { x, y } = req.body
    res.json({
        result: x + y,
    })
    res.status(200).send(`Addition!`)
}
