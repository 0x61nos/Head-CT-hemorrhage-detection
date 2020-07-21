from sklearn.tree import DecisionTreeClassifier
import Draw


def decisionTreeClassifier(X_train, y_train, X_test, y_test, images, index):
    DtreeClf = DecisionTreeClassifier()
    DtreeClf.fit(X_train, y_train)
    acc = DtreeClf.score(X_test, y_test) * 100
    print("---------------------Decision-Tree--------------------------")
    #Draw.drawPredict(DtreeClf, X_test, y_test, images, index)
    print("Decision-Tree: raw pixel accuracy: {:.2f}%".format(acc))
    return acc