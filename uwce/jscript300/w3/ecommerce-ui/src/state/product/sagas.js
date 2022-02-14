import { put, fork, takeLatest, call } from 'redux-saga/effects';
import { FETCH_PRODUCTS } from "../actionTypes";
import * as productApi from '../../libs/product/api';
import { fetchProductsSuccess, fetchProductsFailure } from './actions';

export function* fetchProducts(action) {
  try {
    const products = yield call(productApi.fetchAll);
    // console.log('products', products);
    yield put(fetchProductsSuccess(products));
  } catch(error) {
    yield put(fetchProductsFailure(error));
  }
}

export function* watchFetchProducts() {
  yield takeLatest(FETCH_PRODUCTS, fetchProducts);
}

export default function* () {
  // console.log('inside saga');
  yield fork(watchFetchProducts);
}