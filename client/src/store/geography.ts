import { Module, VuexModule, Mutation, Action } from 'vuex-module-decorators'
import { GeoLayer } from '../../@types/GeoLayer'
import { Bounds, geoJSON } from 'leaflet'
import { GeoJsonProperties } from 'geojson'

const context = require.context('@/assets/', true, /\.geojson\.json$/)
const geoLayers = context.keys().map(filename => {
  const name = filename.split('.')[1].split('/')[1]
  const content = context(filename)
  return { type: name, json: content, label: content.level }
}, {})

@Module({ namespaced: true })
export default class Geography extends VuexModule {
  /**
   * Selected item.
   */
  public selectedItem: GeoJsonProperties = null

  /**
   * Type of geographical layering.
   */
  public layeringType: string = geoLayers[0].type

  /**
   * Current layer.
   */
  public layer: GeoLayer = Object.freeze(geoLayers[0])

  /**
   * Available geo layerings.
   */
  public layers: readonly GeoLayer[] = Object.freeze(geoLayers)

  /**
   * Geographical bounds for each layer.
   */
  public bounds: { [key: string]: Bounds } = Geography.getBounds(geoLayers[0])

  /**
   * Select an item.
   */
  @Mutation
  public __select(item: GeoJsonProperties) {
    this.selectedItem = Object.freeze(item)
  }

  /**
   * Select an item.
   */
  @Action({ commit: '__select' })
  public select(item: GeoJsonProperties) {
    return item
  }

  /**
   * Set the layering type.
   */
  @Mutation
  public __setLayeringType(type: string) {
    this.layer = Object.freeze(this.layers.find(geoLayering => geoLayering.type === type))
    this.bounds = Geography.getBounds(this.layer)
    this.layeringType = type
  }

  /**
   * Deselect an item.
   */
  @Action({ commit: '__setLayeringType' })
  public setLayeringType(type: string) {
    return type
  }

  /**
   * Set bounds depending on layer type.
   */
  public static getBounds (layer: GeoLayer) {
    return geoJSON(layer.json).getLayers().reduce((all, layer) => {
    //@ts-ignore
    all[layer.feature.properties.nom] = layer.getBounds()
    return all
  }, {})
  }
}
