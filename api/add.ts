import { NowRequest, NowResponse } from '@now/node';

export default (req: NowRequest, res: NowResponse) => {
    const { x, y } = req.body;
    res.status(200).json({ result: x + y });
}