// Recursion

function findMax(arr, index = 0, max = null) {
    if (max === null && arr.length > 0) {
        max = arr[0];
    } else if (arr.length === 0) {
        return undefined;
    }

    if (index === arr.length) {
        return max;
    }
    if (max < arr[index]) {
        max = arr[index];
    }

    console.log(max);

    return findMax(arr, index + 1, max);
}
