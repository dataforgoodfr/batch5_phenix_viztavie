import { Emmitter } from './Emmitter'
import { Receiver } from './Receiver'
import { FoodGroup } from './FoodGroup'
import { Command } from './Command'
import { Order } from './Order'

export type Data = {
  emmitters: Emmitter[]
  receivers: Receiver[]
  aggregated_orders: Order[]
  commands: Command[]
  foodgroups: FoodGroup[]
}
