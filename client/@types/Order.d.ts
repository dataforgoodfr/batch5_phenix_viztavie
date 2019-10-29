import { Emmitter } from './Emmitter'
import { Receiver } from './Receiver'

export type Order = {
  count: number
  ec_id: Emmitter['id']
  ec_name: Emmitter['name']
  from: Emmitter['coordinates']
  rc_id: Receiver['id']
  rc_name: Receiver['name']
  to: Receiver['coordinates']
}
