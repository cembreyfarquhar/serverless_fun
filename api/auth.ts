import { NowRequest, NowResponse } from '@now/node';

export default (req: NowRequest, res: NowResponse) => {
    const { username, password } = req.body;
    if (username === 'yes'){
        res.status(201).json({ username, password });
    } else {
        res.status(400).json({ error: "Invalid creds" })
    }
}