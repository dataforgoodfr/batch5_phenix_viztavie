import { GeoJsonObject } from 'geojson'

export type GeoLayer = {
  type: string
  json: GeoJsonObject
  label: string
}
