class Bucket:
    thresh = 20
    values=[[0,0,0]]

    def insert_value(pixel):
        insert = True
        for value in Bucket.values:
            distance = 0
            for i in range{3}:
                distance += abs(value[i]-pixel[i])
            if distance <= Bucket.thresh:
                insert = False
        if insert:
            values.append(pixel)
