import { Emmitter } from './Emmitter'
import { Receiver } from './Receiver'

export type Command = {
  date: number
  ec_id: Emmitter['id']
  rc_id: Receiver['id']
  details: [number, number][]
}
