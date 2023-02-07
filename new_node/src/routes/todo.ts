import express, {Request, Response} from 'express'
import { MeiliSearch } from 'meilisearch'

const router = express.Router()
const client = new MeiliSearch({ host: 'http://meilisearch:7700' })

router.get('/profiles', (req: Request, res: Response) => {
    const query = req.query
    const searchh = query.q
    client.index('data_new').search(`${searchh}`)
        .then((data) => res.send(data))
        .catch((error) => res.send(error))
})

router.get('/papers', (req: Request, res: Response) => {
    const query = req.query
    const searchh = query.q
    client.index('data_pdfs').search(`${searchh}`)
        .then((data) => res.send(data))
        .catch((error) => res.send(error))
})

export {router as todoRouter}


// new todo({title:'new title', description: 'some description'})

