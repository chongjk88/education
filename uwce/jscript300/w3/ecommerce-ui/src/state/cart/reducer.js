import {
  FETCH_CART,
  FETCH_CART_SUCCESS,
  FETCH_CART_FAILURE,
  ADD_TO_CART,
  ADD_TO_CART_SUCCESS,
  ADD_TO_CART_FAILURE,
} from '../actionTypes';

const initialState = {
  isLoading: false,
  cart: { items: [] },
  error: null,
};

export default (state = initialState, action) => {
  switch(action.type) {
    case FETCH_CART:
    case ADD_TO_CART:
      return {
        ...state,
        isLoading: true,
      };
      
    case FETCH_CART_SUCCESS:
    case ADD_TO_CART_SUCCESS:
      return {
        ...state,
        isLoading: false,
        cart: action.cart,
      };

    case FETCH_CART_FAILURE:
    case ADD_TO_CART_FAILURE:
      return {
        ...state,
        isLoading: false,
        error: action.error,
      };

    default:
      return state;
  }
}