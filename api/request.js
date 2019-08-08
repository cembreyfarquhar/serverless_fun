import axios from 'axios'

module.exports = async (req, res) => {
    // const { x, y } = req.body
    const response = await axios.get(
        'https://jsonplaceholder.typicode.com/todos/1',
    )
    const { data } = response
    res.status(201).json(data)
}
