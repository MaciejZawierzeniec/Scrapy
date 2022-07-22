import csv


class ComputersPipeline:
    def process_item(self, item, spider):
        with open('data.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(dict(item).values())
