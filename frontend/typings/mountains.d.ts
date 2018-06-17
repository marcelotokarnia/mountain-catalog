interface IDataMountains {
  mountains: IMountains[]
}

interface IMountains {
  name: string
  elevation: number
  lat: number
  lng: number
  distance: number
}

export {
  IMountains,
  IDataMountains,
}
