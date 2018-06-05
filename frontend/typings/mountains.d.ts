import {Geometry} from './geometry.d'

interface MountainProperties {
  name: string
  elevation: number
  distance: number
}

interface MountainsGraphql {
  properties: MountainProperties
  geometry: Geometry
}

interface MountainsFrontend {
  name: string
  elevation: number
  lat: number
  lng: number
  distance: number
}

export {
  MountainsGraphql,
  MountainsFrontend
}