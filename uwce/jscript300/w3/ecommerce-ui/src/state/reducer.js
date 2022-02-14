import { combineReducers } from 'redux';
import productReducer from './product/reducer';
import cartReducer from './cart/reducer';

export default combineReducers({
  product: productReducer,
  cart: cartReducer,
});