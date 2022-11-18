export default function transactionsComparator(t1, t2) {
  return datesComparator(t1.date, t2.date);
}

function datesComparator(d1, d2) {
  if (d1 > d2) {
    return -1;
  } else if (d2 > d1) {
    return 1;
  } else {
    return 0;
  }
}
