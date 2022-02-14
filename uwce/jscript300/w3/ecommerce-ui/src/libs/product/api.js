import mockProducts from './products.mock';

export const fetchAll = async () => mockProducts;

// export const fetchAll = async () => {
//   throw {message: 'Product is not found.'}
// }