import { Module, VuexModule, Mutation, Action } from 'vuex-module-decorators'
import FoodGroup from './../../@types/FoodGroup'

@Module({ namespaced: true })
export default class Categories extends VuexModule {
  /**
   * Selected category.
   */
  public selectedItem: string = null

  /**
   * Optimal repartition (in g).
   */
  public readonly optimalRepartition: { [key: string]: number } = {
    Fruits: 165,
    Légumes: 165,
    'Produits laitiers (hors fromage)': 225,
    Fromage: 25,
    'Féculents raffinés': 125,
    'Féculents non raffinés': 90,
    'Viande, oeufs': 225,
    Poisson: 30,
    'Matières grasses ajoutées': 25,
    'Produits gras sucrés salés': 25
  }

  /**
   * Colors for each category.
   */
  public readonly colors: { [key: string]: string } = {
    Fruits: '#2e86de',
    Légumes: '#54a0ff',
    'Produits laitiers (hors fromage)': '#1dd1a1',
    Fromage: '#10ac84',
    'Féculents raffinés': '#ff6b6b',
    'Féculents non raffinés': '#ee5253',
    'Viande, oeufs': '#feca57',
    Poisson: '#ff9f43',
    'Matières grasses ajoutées': '#5f27cd',
    'Produits gras sucrés salés': '#341f97'
  }

  /**
   * Select an item.
   */
  @Mutation
  public __select(item: string) {
    this.selectedItem = item
  }

  /**
   * Select an item.
   */
  @Action({ commit: '__select' })
  public select(item: string) {
    return item
  }
}
