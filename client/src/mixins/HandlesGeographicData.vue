<script lang="ts">
import { Component, Vue, Watch } from 'vue-property-decorator'
import { Emmitter } from '../../@types/Emmitter'
import { Receiver } from '../../@types/Receiver'
import L, { Bounds } from 'leaflet'
import { Order } from '../../@types/Order'
import { Data } from '../../@types/Data'

//@ts-ignore
const context = require.context('@/assets/', true, /\.geojson\.json$/)
const geoLayerings = context.keys().map(filename => {
  const name = filename.split('.')[1].split('/')[1]
  const content = context(filename)
  return { type: name, json: content, label: content.level }
}, {})

@Component
export default class HandlesGeographicData extends Vue {
  /**
   * Selected geographic item.
   */
  public selectedGeoItem: any = null

  /**
   * Type of geographical layering.
   */
  public geoLayeringType: string = 'regions'

  /**
   * Available geo layerings.
   */
  public geoLayerings = Object.freeze(geoLayerings)

  /**
   * Geojson of geographical layering.
   */
  get geoLayering() {
    return this.geoLayerings.find(
      geoLayering => geoLayering.type === this.geoLayeringType
    )
  }

  /**
   * Filter emmitters and receivers by geographical bounds.
   */
  public isWithinBounds(subjects: Emmitter[] | Receiver[], bounds: Bounds) {
    return subjects.filter(subject => {
      return (
        subject.coordinates.every(p => p !== null) &&
        bounds.contains(subject.coordinates)
      )
    })
  }

  /**
   * Get geo data by key.
   */
  public getGeoData(key: string) {
    return this.selectedGeoItem
      ? this.selectedGeoItem.properties[key]
      : this[key]
  }

  /**
   * Add properties to geo layering.
   */
  public addPropertiesToGeoLayering(data: Data) {
    return geoLayerings.map(geoLayering => {
      return L.geoJSON(geoLayering.json)
        .getLayers()
        .map((layer: any) => {
          const bounds = layer.getBounds()
          const emmitters = this.isWithinBounds(data.emmitters, bounds)
          const receivers = this.isWithinBounds(data.receivers, bounds)
          const orders = data.aggregated_orders.filter(order =>
            emmitters.find(emmitter => emmitter.id === order.ec_id)
          )

          layer.feature.properties = {
            ...layer.feature.properties,
            bounds: bounds,
            emmitters: emmitters,
            receivers: receivers,
            orders: orders
          }

          return layer
        })
    })
  }
}
</script>