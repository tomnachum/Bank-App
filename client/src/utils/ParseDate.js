export default function parseDate(dateStr) {
  const [date, time] = dateStr.split(" ");
  const [year, month, day] = date.split("-");
  const [hours, minutes, seconds] = time.split(":");
  return new Date(+year, +month, +day, +hours, +minutes, +seconds);
}
