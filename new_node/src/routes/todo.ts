import express, {Request, Response} from 'express'
import { MeiliSearch } from 'meilisearch'

const router = express.Router()
const client = new MeiliSearch({ host: 'http://meilisearch:7700' })

router.get('/api/todo', (req: Request, res: Response) => {
    const query = req.query
    const searchh = query.search
    client.index('data').search(`${searchh}`)
        .then((data) => res.send(data))
        .catch((error) => res.send(error))
})

router.post('api/todo', (req, res) => {
    return res.send('new todo created')
})

export {router as todoRouter}


// new todo({title:'new title', description: 'some description'})

